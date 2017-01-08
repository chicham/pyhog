#include <vector>

#define eps 0.0001

class FeatureVector{
public:
    inline FeatureVector() {};
    inline FeatureVector(const std::vector<double> &data, const int rows, const int cols, const int size) : data(data), rows(rows), cols(cols), size(size) {}
    std::vector<double> data;
    int rows;
    int cols;
    int size;
};


FeatureVector process(double* im, const int rows, const int cols, const int depth, const int sbin);
